#!/usr/bin/python3
'''Class Base'''
import json
import csv
import turtle
import os


class Base:
    """Class that defines properties of Base.

     Attributes:
        id (int): Identity of each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new instances of Base.

        Args:
            id (int, optional): Identity of each instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        filename = "{}.json".format(cls.__name__)
        list_dic = (
            [obj.to_dictionary() for obj in list_objs]
            if list_objs
            else []
        )
        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of objects from JSON string representation'''
        if json_string is None or not json_string:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        return (dummy)

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''serializes list_objs to a CSV file'''
        filename = "{}.csv".format(cls.__name__)

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])

                elif cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''deserializes list_objs from a CSV file'''
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                objects_data = [list(map(int, row)) for row in csv_reader]
        except FileNotFoundError:
            return []

        instances = []
        for data in objects_data:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
                instance.update(
                    id=data[0],
                    width=data[1],
                    height=data[2],
                    x=data[3],
                    y=data[4]
                )
            elif cls.__name__ == "Square":
                instance = cls(1)
                instance.update(id=data[0], size=data[1], x=data[2], y=data[3])
            else:
                raise ValueError(f"Unsupported class: {cls.__name__}")

            instances.append(instance)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''opens a window and draws all the Rectangles and Squares'''
        turtle.speed(2)

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)
            turtle.forward(rect.width)
            turtle.right(90)
            turtle.forward(rect.height)
            turtle.right(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.exitonclick()
