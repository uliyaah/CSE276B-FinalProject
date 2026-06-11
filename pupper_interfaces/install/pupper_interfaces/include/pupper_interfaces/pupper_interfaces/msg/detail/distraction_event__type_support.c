// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pupper_interfaces:msg/DistractionEvent.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pupper_interfaces/msg/detail/distraction_event__rosidl_typesupport_introspection_c.h"
#include "pupper_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pupper_interfaces/msg/detail/distraction_event__functions.h"
#include "pupper_interfaces/msg/detail/distraction_event__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pupper_interfaces__msg__DistractionEvent__init(message_memory);
}

void pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_fini_function(void * message_memory)
{
  pupper_interfaces__msg__DistractionEvent__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_member_array[1] = {
  {
    "duration",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pupper_interfaces__msg__DistractionEvent, duration),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_members = {
  "pupper_interfaces__msg",  // message namespace
  "DistractionEvent",  // message name
  1,  // number of fields
  sizeof(pupper_interfaces__msg__DistractionEvent),
  pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_member_array,  // message members
  pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_init_function,  // function to initialize message memory (memory has to be allocated)
  pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_type_support_handle = {
  0,
  &pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pupper_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pupper_interfaces, msg, DistractionEvent)() {
  if (!pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_type_support_handle.typesupport_identifier) {
    pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pupper_interfaces__msg__DistractionEvent__rosidl_typesupport_introspection_c__DistractionEvent_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
