// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pupper_interfaces:msg/Command.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__COMMAND__TRAITS_HPP_
#define PUPPER_INTERFACES__MSG__DETAIL__COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pupper_interfaces/msg/detail/command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pupper_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Command & msg,
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
  const Command & msg,
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

inline std::string to_yaml(const Command & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace pupper_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pupper_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pupper_interfaces::msg::Command & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::msg::Command & msg)
{
  return pupper_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::msg::Command>()
{
  return "pupper_interfaces::msg::Command";
}

template<>
inline const char * name<pupper_interfaces::msg::Command>()
{
  return "pupper_interfaces/msg/Command";
}

template<>
struct has_fixed_size<pupper_interfaces::msg::Command>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pupper_interfaces::msg::Command>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pupper_interfaces::msg::Command>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PUPPER_INTERFACES__MSG__DETAIL__COMMAND__TRAITS_HPP_
