from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from base.models import Item
from base.models import Profile
from base.serializers import ItemSerializer
from base.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime

import base64
from django.core.files.base import ContentFile

class ItemViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows items to be viewed or edited.
    """
	queryset = Item.objects.all().order_by('-created_at')
	serializer_class = ItemSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def perform_create(self, serializer):
		location = self.request.data.get('location');
		date = self.request.data.get('date');
		tags = self.request.data.get('tags');
		image = None
		if self.request.data.get('image'):
			image = self.request.data.get('image');
			if type(image) is str:
				format, imgstr = image.split(';base64,')
				ext = format.split('/')[-1]
				image = ContentFile(base64.b64decode(imgstr), name='item.' + ext) # You can save this as file instance.
		# serializer.save(featured_img=self.request.data.get('image'), created_by=self.request.user, date = date, location = location, tags = tags)
		serializer.save(featured_img=image, created_by=self.request.user, date = date, location = location, tags = tags)



def newsfeed(request):
	"""
    API endpoint that returned newsfeed.
    """
	if request.method == 'GET':
		return JsonResponse(serializer.errors, status=400)
	return HttpResponse("GET method not allowed")

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def profile(request, id = ''):
	"""
    API endpoint that returns profile page.
    """
	if id:
		try:
			user = User.objects.get(pk=id)
		except User.DoesNotExist:
			user = None
	else:
		user = request.user
	if not user:
		return HttpResponse("User not found with given id: " + id, status = 404)

	if request.method == 'GET':
		response_data = {}
		response_data["username"] = user.username
		response_data["email"] = user.email
		if hasattr(user, 'profile'):
			response_data["fullName"] = user.profile.fullName
			response_data["birthday"] = user.profile.birthday
			response_data["location"] = user.profile.location
			try:
				response_data["photo"] = request.META['HTTP_HOST'] + user.profile.photo.url
			except:
				response_data["photo"] = None
		return JsonResponse(response_data)
	else:
		response_data = {}
		photo_ch = False
		data = JSONParser().parse(request)
		for key in data:
			if key == "username":
				response_data["username"] = data.get(key)
				user.username = data.get(key)
			if key == "email":
				response_data["email"] = data.get(key)
				user.email = data.get(key)
			if hasattr(user,"profile"):
				if key == "birthday":
					try:
						datetime.datetime.strptime(data.get(key), '%Y-%m-%d')
						user.profile.birthday = data.get(key)
						response_data["birthday"] = data.get(key)
					except:
						return HttpResponse("Value has an invalid date format. It must be in YYYY-MM-DD format.", status = 400)
				if key == "location":
					response_data["location"] = data.get(key)
					user.profile.location = data.get(key)
				if key == "photo":
					image = data.get(key)
					if type(image) is str:
						format, imgstr = image.split(';base64,')
						ext = format.split('/')[-1]
						image = ContentFile(base64.b64decode(imgstr), name='item.' + ext)
					user.profile.photo = image
					photo_ch = True
				if key == "fullName":
					user.profile.fullName = data.get(key)
					response_data["fullName"] = data.get(key)
		user.save()
		if(photo_ch):
			response_data["photo"] = request.META['HTTP_HOST']+user.profile.photo.url

		return JsonResponse(response_data)

