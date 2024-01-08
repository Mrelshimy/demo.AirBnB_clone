#!/usr/bin/env python3
""" Base Model Class Module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
	"""Base Model Class"""

	def __init__(self, *args, **kwargs):
		"""Constructor"""
		if not kwargs:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = BaseModel.save(self)
			storage.new(self)
		else:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					value = datetime.fromisoformat(value)
				if key == '__class__':
					continue
				else:
					setattr(self, key, value)

	def __str__(self):
		"""Return String representation of an object"""
		return f"[{type(self).__name__}] ({self.id}) {str(self.__dict__)}"


	def save(self):
		"""Update Updated_at to current datetime"""
		storage.save(self)
		return datetime.now()

	def to_dict(self):
		"""Return a Dictionary representation of an object"""
		o_dict = self.__dict__
		o_dict['created_at'] = datetime.isoformat(self.created_at)
		o_dict['updated_at'] = datetime.isoformat(self.updated_at)
		o_dict['__class__'] = self.__class__.__name__
		return o_dict