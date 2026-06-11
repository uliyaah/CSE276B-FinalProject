// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pupper_interfaces:srv/StopMusic.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__STOP_MUSIC__STRUCT_H_
#define PUPPER_INTERFACES__SRV__DETAIL__STOP_MUSIC__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/StopMusic in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__StopMusic_Request
{
  uint8_t structure_needs_at_least_one_member;
} pupper_interfaces__srv__StopMusic_Request;

// Struct for a sequence of pupper_interfaces__srv__StopMusic_Request.
typedef struct pupper_interfaces__srv__StopMusic_Request__Sequence
{
  pupper_interfaces__srv__StopMusic_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__StopMusic_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/StopMusic in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__StopMusic_Response
{
  /// Indicates whether the command was executed successfully
  bool success;
  /// Additional information or error message
  rosidl_runtime_c__String message;
} pupper_interfaces__srv__StopMusic_Response;

// Struct for a sequence of pupper_interfaces__srv__StopMusic_Response.
typedef struct pupper_interfaces__srv__StopMusic_Response__Sequence
{
  pupper_interfaces__srv__StopMusic_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__StopMusic_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUPPER_INTERFACES__SRV__DETAIL__STOP_MUSIC__STRUCT_H_
