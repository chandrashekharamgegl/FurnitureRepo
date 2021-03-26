from django.test import TestCase
from rest_framework import status
from django.urls import reverse_lazy
from factory_app.models import TableLeg, Table, Leg, Feet
from factory_app.serializers import TableLegSerializer, TableSerializer, LegSerializer, FeetSerializer

# Create your tests here.



class TablesTest(TestCase):
    '''Testing Table Model'''

    def setUp(self):
        self.url = '/table/'
        self.url_with_id = '/table/1/'

        self.feet_obj1 = Feet.objects.create(width=24, length=13)
        self.feet_obj2 = Feet.objects.create(radius=24)

        self.leg_obj1 = Leg.objects.create(feet=self.feet_obj1)

        self.leg_obj2 = Leg.objects.create(feet=self.feet_obj2)

        self.leg_obj3 = Leg.objects.create(feet=self.feet_obj2)
        self.leg_obj4 = Leg.objects.create(feet=self.feet_obj1)
        self.leg_obj5 = Leg.objects.create(feet=self.feet_obj2)

        self.leg_obj_delete = Leg.objects.create(feet=self.feet_obj2)


    def test_create(self):
        '''Table object creation test'''
        data = {"name": "Table_test_num_1"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Table.objects.count(), 1)

        data = {"leg":1, "table":1}
        response = self.client.post('/table-leg/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TableLeg.objects.count(), 1)

    def test_list(self):
        '''Table objects listing test'''
        response = self.client.get(self.url, format='json')
        table_objs = Table.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TableSerializer(table_objs, many=True).data)
        
        response = self.client.get('/table-leg/', format='json')
        table_leg_objs = TableLeg.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TableLegSerializer(table_leg_objs, many=True).data)

    def test_detail(self):
        """Get single table object test"""
        table_obj = Table.objects.create(name="Table_test_detail_1")
        response = self.client.get(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TableSerializer(table_obj).data)

        table_leg_obj = TableLeg.objects.create(leg=self.leg_obj1, table=table_obj)
        response = self.client.get('/table-leg/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TableLegSerializer(table_leg_obj).data)


    def test_update(self):
        """Fully updating table object test"""
        table_obj = Table.objects.create(name="Table_test_1")
        updated_data = {"name": "Table_test_update_11", "leg": 4}
        response = self.client.put(self.url_with_id, updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), updated_data.get('name'))
    
        table_leg_obj = TableLeg.objects.create(leg=self.leg_obj3, table=table_obj)
        table_obj = Table.objects.create(name="Table_test_2")
        updated_tl_data = {"leg": 4, "table":2}
        response = self.client.put('/table-leg/1/', updated_tl_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('leg'), updated_tl_data.get('leg'))
        self.assertEqual(response.data.get('table'), updated_tl_data.get('table'))


    def test_update_partial(self):
        """Partially updating table object test"""
        table_obj = Table.objects.create(name="Table_test_2")
        updated_data = {"name": "Table_test_update_22"}
        response = self.client.patch(self.url_with_id, updated_data,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), updated_data.get('name'))

        table_leg_obj = TableLeg.objects.create(leg=self.leg_obj2, table=table_obj)
        updated_tl_data = {"leg":1}
        response = self.client.patch('/table-leg/1/', updated_tl_data,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('leg'), updated_tl_data.get('leg'))



    def test_delete(self):
        """ Table object deletion test """
        table_obj_delete = Table.objects.create(name="Table_test_delete_1")

        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Table.objects.count(), 0) 

        table_obj = Table.objects.create(name="Table_test_delete_2")
        table_leg_obj = TableLeg.objects.create(leg=self.leg_obj_delete, table=table_obj)
        response = self.client.delete('/table-leg/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TableLeg.objects.count(), 0) 





class LegsTest(TestCase):
    '''Testing Leg Model'''

    def setUp(self):
        self.url = '/leg/'
        self.url_with_id = '/leg/1/'

        self.feet_obj1 = Feet.objects.create(width=24, length=13)
        self.feet_obj2 = Feet.objects.create(radius=36)
        self.feet_obj3 = Feet.objects.create(width=24, length=13)

    def test_create(self):
        '''Leg object creation test'''
        data = {"feet": 1}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leg.objects.count(), 1)


    def test_list(self):
        '''Leg objects listing test'''
        response = self.client.get(self.url, format='json')
        leg_objs = Leg.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, LegSerializer(leg_objs, many=True).data)


    def test_detail(self):
        '''Get single leg object test'''
        leg_obj = Leg.objects.create(feet=self.feet_obj1)
        response = self.client.get(self.url_with_id, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, LegSerializer(leg_obj).data)

    def test_update(self):
        """Fully updating leg object test"""
        leg_obj = Leg.objects.create(feet=self.feet_obj2)
        updated_data = {"feet": 3}
        response = self.client.put(self.url_with_id, updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('leg'), updated_data.get('leg'))

    def test_update_partial(self):
        """Partially updating feet object test"""
        leg_obj = Leg.objects.create(feet=self.feet_obj3)
        updated_data = {"feet": 2}
        response = self.client.patch(self.url_with_id, updated_data,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('leg'), updated_data.get('leg'))


    def test_delete(self):
        """ Leg object deletion test """    
        leg_obj = Leg.objects.create(feet=self.feet_obj3)
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Leg.objects.count(), 0)





class FeetTest(TestCase):
    '''Testing Feet Model'''

    def setUp(self):
        self.url = '/feet/'
        self.url_with_id = '/feet/1/'

    def test_create_circle(self):
        """Circle feet creation test"""
        data = {'radius': 24}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feet.objects.count(), 1)

    def test_create_rectangle(self):
        """Rectangle feet creation test"""
        data = {'width': 24, 'length': 13}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feet.objects.count(), 1)

    def test_invalid_data(self):
        """Invalid data for feet model test"""
        # A foot with a radius must not have length or width.
        data = {'radius': 24, 'length': 13}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # A foot with a length must also have a width.
        data = {'width': "", 'length': 13}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        #A foot with a width must also have a length.
        data = {'width': 24, 'length': ""}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_list(self):
        """Listing data for feet model test"""
        response = self.client.get(self.url, format='json')
        feet_objs = Feet.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, FeetSerializer(feet_objs, many=True).data)


    def test_detail(self):
        """Get single feet object test"""
        feet_obj = Feet.objects.create(width=30, length=45)
        response = self.client.get(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, FeetSerializer(feet_obj).data)

    def test_update(self):
        """Fully updating feet object test"""
        feet_obj = Feet.objects.create(width=26, length=24)
        updated_data = {"width":36, "length": 28}
        response = self.client.put(self.url_with_id, updated_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('width'), updated_data.get('width'))
        self.assertEqual(response.data.get('length'), updated_data.get('length'))
        
    def test_update_partial(self):
        """Partially updating feet object test"""
        feet_obj = Feet.objects.create(width=24, length=22)
        updated_data = {'width': 30, "length": 22}
        response = self.client.patch(self.url_with_id, updated_data,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('width'), updated_data.get('width'))


    def test_delete(self):
        """ Feet object deletion test """
        feet_obj = Feet.objects.create(radius=48)
        response = self.client.delete(self.url_with_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feet.objects.count(), 0) 

