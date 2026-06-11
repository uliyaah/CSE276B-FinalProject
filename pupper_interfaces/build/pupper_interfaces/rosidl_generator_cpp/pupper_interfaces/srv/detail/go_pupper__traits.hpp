// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pupper_interfaces:srv/GoPupper.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__TRAITS_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pupper_interfaces/srv/detail/go_pupper__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoPupper_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoPupper_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoPupper_Request & msg, bool use_flow_style = false)
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
  const pupper_interfaces::srv::GoPupper_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::GoPupper_Request & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::GoPupper_Request>()
{
  return "pupper_interfaces::srv::GoPupper_Request";
}

template<>
inline const char * name<pupper_interfaces::srv::GoPupper_Request>()
{
  return "pupper_interfaces/srv/GoPupper_Request";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::GoPupper_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::GoPupper_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pupper_interfaces::srv::GoPupper_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoPupper_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: executed
  {
    out << "executed: ";
    rosidl_generator_traits::value_to_yaml(msg.executed, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoPupper_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: executed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "executed: ";
    rosidl_generator_traits::value_to_yaml(msg.executed, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoPupper_Response & msg, bool use_flow_style = false)
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
  const pupper_interfaces::srv::GoPupper_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::GoPupper_Response & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::GoPupper_Response>()
{
  return "pupper_interfaces::srv::GoPupper_Response";
}

template<>
inline const char * name<pupper_interfaces::srv::GoPupper_Response>()
{
  return "pupper_interfaces/srv/GoPupper_Response";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::GoPupper_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::GoPupper_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pupper_interfaces::srv::GoPupper_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<pupper_interfaces::srv::GoPupper>()
{
  return "pupper_interfaces::srv::GoPupper";
}

template<>
inline const char * name<pupper_interfaces::srv::GoPupper>()
{
  return "pupper_interfaces/srv/GoPupper";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::GoPupper>
  : std::integral_constant<
    bool,
    has_fixed_size<pupper_interfaces::srv::GoPupper_Request>::value &&
    has_fixed_size<pupper_interfaces::srv::GoPupper_Response>::value
  >
{
};

template<>
struct has_bounded_size<pupper_interfaces::srv::GoPupper>
  : std::integral_constant<
    bool,
    has_bounded_size<pupper_interfaces::srv::GoPupper_Request>::value &&
    has_bounded_size<pupper_interfaces::srv::GoPupper_Response>::value
  >
{
};

template<>
struct is_service<pupper_interfaces::srv::GoPupper>
  : std::true_type
{
};

template<>
struct is_service_request<pupper_interfaces::srv::GoPupper_Request>
  : std::true_type
{
};

template<>
struct is_service_response<pupper_interfaces::srv::GoPupper_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__TRAITS_HPP_
