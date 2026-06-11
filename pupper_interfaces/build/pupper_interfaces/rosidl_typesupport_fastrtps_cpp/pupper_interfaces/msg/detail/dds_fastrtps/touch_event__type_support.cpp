// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice
#include "pupper_interfaces/msg/detail/touch_event__rosidl_typesupport_fastrtps_cpp.hpp"
#include "pupper_interfaces/msg/detail/touch_event__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace pupper_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pupper_interfaces
cdr_serialize(
  const pupper_interfaces::msg::TouchEvent & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: location
  cdr << ros_message.location;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pupper_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  pupper_interfaces::msg::TouchEvent & ros_message)
{
  // Member: location
  cdr >> ros_message.location;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pupper_interfaces
get_serialized_size(
  const pupper_interfaces::msg::TouchEvent & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: location
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.location.size() + 1);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pupper_interfaces
max_serialized_size_TouchEvent(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: location
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = pupper_interfaces::msg::TouchEvent;
    is_plain =
      (
      offsetof(DataType, location) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _TouchEvent__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const pupper_interfaces::msg::TouchEvent *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TouchEvent__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<pupper_interfaces::msg::TouchEvent *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TouchEvent__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const pupper_interfaces::msg::TouchEvent *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TouchEvent__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_TouchEvent(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _TouchEvent__callbacks = {
  "pupper_interfaces::msg",
  "TouchEvent",
  _TouchEvent__cdr_serialize,
  _TouchEvent__cdr_deserialize,
  _TouchEvent__get_serialized_size,
  _TouchEvent__max_serialized_size
};

static rosidl_message_type_support_t _TouchEvent__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TouchEvent__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace pupper_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_pupper_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<pupper_interfaces::msg::TouchEvent>()
{
  return &pupper_interfaces::msg::typesupport_fastrtps_cpp::_TouchEvent__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pupper_interfaces, msg, TouchEvent)() {
  return &pupper_interfaces::msg::typesupport_fastrtps_cpp::_TouchEvent__handle;
}

#ifdef __cplusplus
}
#endif
