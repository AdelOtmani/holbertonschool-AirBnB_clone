#!/usr/bin/python3
"""Project AirBnB holberton A. Otmani
    """


from datetime import datetime
from uuid import uuid4


class BaseModel():
    """base class initialisation
    """

    def __init__(self, *args, **kwargs):
        """Initialisation of BaseModel

            Args:
                *args : argument gives
                **kwargs:  Key/Value of dict attributs
        """
        self.id = str(uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                elif key != "__class__":
                    self.__dict__[key] = value


    def save(self):
        """updated_at: updates the public instance attribute updated_at with the current datetime

                 datetime - when an instance is created and
                            it will be updated every time you change your object

        """
        self.updated_at = datetime.today()

    def __str__(self):
        """return str

        Returns:
            should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Returns:
           a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict

