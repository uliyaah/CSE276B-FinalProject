# generated from rosidl_generator_py/resource/_idl.py.em
# with input from pupper_interfaces:srv/CameraPupper.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CameraPupper_Request(type):
    """Metaclass of message 'CameraPupper_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pupper_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pupper_interfaces.srv.CameraPupper_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__camera_pupper__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__camera_pupper__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__camera_pupper__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__camera_pupper__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__camera_pupper__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CameraPupper_Request(metaclass=Metaclass_CameraPupper_Request):
    """Message class 'CameraPupper_Request'."""

    __slots__ = [
        '_duration',
    ]

    _fields_and_field_types = {
        'duration': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.duration = kwargs.get('duration', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.duration != other.duration:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def duration(self):
        """Message field 'duration'."""
        return self._duration

    @duration.setter
    def duration(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'duration' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'duration' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._duration = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_CameraPupper_Response(type):
    """Metaclass of message 'CameraPupper_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pupper_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pupper_interfaces.srv.CameraPupper_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__camera_pupper__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__camera_pupper__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__camera_pupper__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__camera_pupper__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__camera_pupper__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CameraPupper_Response(metaclass=Metaclass_CameraPupper_Response):
    """Message class 'CameraPupper_Response'."""

    __slots__ = [
        '_executed',
    ]

    _fields_and_field_types = {
        'executed': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.executed = kwargs.get('executed', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.executed != other.executed:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def executed(self):
        """Message field 'executed'."""
        return self._executed

    @executed.setter
    def executed(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'executed' field must be of type 'bool'"
        self._executed = value


class Metaclass_CameraPupper(type):
    """Metaclass of service 'CameraPupper'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('pupper_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pupper_interfaces.srv.CameraPupper')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__camera_pupper

            from pupper_interfaces.srv import _camera_pupper
            if _camera_pupper.Metaclass_CameraPupper_Request._TYPE_SUPPORT is None:
                _camera_pupper.Metaclass_CameraPupper_Request.__import_type_support__()
            if _camera_pupper.Metaclass_CameraPupper_Response._TYPE_SUPPORT is None:
                _camera_pupper.Metaclass_CameraPupper_Response.__import_type_support__()


class CameraPupper(metaclass=Metaclass_CameraPupper):
    from pupper_interfaces.srv._camera_pupper import CameraPupper_Request as Request
    from pupper_interfaces.srv._camera_pupper import CameraPupper_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
