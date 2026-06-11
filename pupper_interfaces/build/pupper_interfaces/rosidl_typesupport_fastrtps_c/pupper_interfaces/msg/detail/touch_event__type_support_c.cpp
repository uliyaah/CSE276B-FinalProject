// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice
#include "pupper_interfaces/msg/detail/touch_event__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "pupper_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "pupper_interfaces/msg/detail/touch_event__struct.h"
#include "pupper_interfaces/msg/detail/touch_event__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // location
#include "rosidl_runtime_c/string_functions.h"  // location

// forward declare type support functions


using _TouchEvent__ros_msg_type = pupper_interfaces__msg__TouchEvent;

static bool _TouchEvent__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TouchEvent__ros_msg_type * ros_message = static_cast<const _TouchEvent__ros_msg_type *>(untyped_ros_message);
  // Field name: location
  {
    const rosidl_runtime_c__String * str = &ros_message->location;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _TouchEvent__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TouchEvent__ros_msg_type * ros_message = static_cast<_TouchEvent__ros_msg_type *>(untyped_ros_message);
  // Field name: location
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->location.data) {
      rosidl_runtime_c__String__init(&ros_message->location);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->location,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'location'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pupper_interfaces
size_t get_serialized_size_pupper_interfaces__msg__TouchEvent(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TouchEvent__ros_msg_type * ros_message = static_cast<const _TouchEvent__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name location
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->location.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _TouchEvent__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_pupper_interfaces__msg__TouchEvent(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pupper_interfaces
size_t max_serialized_size_pupper_interfaces__msg__TouchEvent(
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

  // member: location
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
    using DataType = pupper_interfaces__msg__TouchEvent;
    is_plain =
      (
      offsetof(DataType, location) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TouchEvent__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_pupper_interfaces__msg__TouchEvent(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TouchEvent = {
  "pupper_interfaces::msg",
  "TouchEvent",
  _TouchEvent__cdr_serialize,
  _TouchEvent__cdr_deserialize,
  _TouchEvent__get_serialized_size,
  _TouchEvent__max_serialized_size
};

static rosidl_message_type_support_t _TouchEvent__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TouchEvent,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pupper_interfaces, msg, TouchEvent)() {
  return &_TouchEvent__type_support;
}

#if defined(__cplusplus)
}
#endif
