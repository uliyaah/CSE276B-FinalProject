// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pupper_interfaces:srv/StateManagerCommand.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__TRAITS_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pupper_interfaces/srv/detail/state_manager_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'command'
#include "pupper_interfaces/msg/detail/command__traits.hpp"

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const StateManagerCommand_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    to_flow_style_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StateManagerCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command:\n";
    to_block_style_yaml(msg.command, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StateManagerCommand_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace pupper_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pupper_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pupper_interfaces::srv::StateManagerCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::StateManagerCommand_Request & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::StateManagerCommand_Request>()
{
  return "pupper_interfaces::srv::StateManagerCommand_Request";
}

template<>
inline const char * name<pupper_interfaces::srv::StateManagerCommand_Request>()
{
  return "pupper_interfaces/srv/StateManagerCommand_Request";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::StateManagerCommand_Request>
  : std::integral_constant<bool, has_fixed_size<pupper_interfaces::msg::Command>::value> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::StateManagerCommand_Request>
  : std::integral_constant<bool, has_bounded_size<pupper_interfaces::msg::Command>::value> {};

template<>
struct is_message<pupper_interfaces::srv::StateManagerCommand_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const StateManagerCommand_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StateManagerCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StateManagerCommand_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace pupper_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pupper_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pupper_interfaces::srv::StateManagerCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::StateManagerCommand_Response & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::StateManagerCommand_Response>()
{
  return "pupper_interfaces::srv::StateManagerCommand_Response";
}

template<>
inline const char * name<pupper_interfaces::srv::StateManagerCommand_Response>()
{
  return "pupper_interfaces/srv/StateManagerCommand_Response";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::StateManagerCommand_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::StateManagerCommand_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pupper_interfaces::srv::StateManagerCommand_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<pupper_interfaces::srv::StateManagerCommand>()
{
  return "pupper_interfaces::srv::StateManagerCommand";
}

template<>
inline const char * name<pupper_interfaces::srv::StateManagerCommand>()
{
  return "pupper_interfaces/srv/StateManagerCommand";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::StateManagerCommand>
  : std::integral_constant<
    bool,
    has_fixed_size<pupper_interfaces::srv::StateManagerCommand_Request>::value &&
    has_fixed_size<pupper_interfaces::srv::StateManagerCommand_Response>::value
  >
{
};

template<>
struct has_bounded_size<pupper_interfaces::srv::StateManagerCommand>
  : std::integral_constant<
    bool,
    has_bounded_size<pupper_interfaces::srv::StateManagerCommand_Request>::value &&
    has_bounded_size<pupper_interfaces::srv::StateManagerCommand_Response>::value
  >
{
};

template<>
struct is_service<pupper_interfaces::srv::StateManagerCommand>
  : std::true_type
{
};

template<>
struct is_service_request<pupper_interfaces::srv::StateManagerCommand_Request>
  : std::true_type
{
};

template<>
struct is_service_response<pupper_interfaces::srv::StateManagerCommand_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__TRAITS_HPP_
