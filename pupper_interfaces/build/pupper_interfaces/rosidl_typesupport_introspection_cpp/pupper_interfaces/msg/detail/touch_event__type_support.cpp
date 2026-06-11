// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "pupper_interfaces/msg/detail/touch_event__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace pupper_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TouchEvent_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) pupper_interfaces::msg::TouchEvent(_init);
}

void TouchEvent_fini_function(void * message_memory)
{
  auto typed_message = static_cast<pupper_interfaces::msg::TouchEvent *>(message_memory);
  typed_message->~TouchEvent();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TouchEvent_message_member_array[1] = {
  {
    "location",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pupper_interfaces::msg::TouchEvent, location),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TouchEvent_message_members = {
  "pupper_interfaces::msg",  // message namespace
  "TouchEvent",  // message name
  1,  // number of fields
  sizeof(pupper_interfaces::msg::TouchEvent),
  TouchEvent_message_member_array,  // message members
  TouchEvent_init_function,  // function to initialize message memory (memory has to be allocated)
  TouchEvent_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TouchEvent_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TouchEvent_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace pupper_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<pupper_interfaces::msg::TouchEvent>()
{
  return &::pupper_interfaces::msg::rosidl_typesupport_introspection_cpp::TouchEvent_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, pupper_interfaces, msg, TouchEvent)() {
  return &::pupper_interfaces::msg::rosidl_typesupport_introspection_cpp::TouchEvent_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
