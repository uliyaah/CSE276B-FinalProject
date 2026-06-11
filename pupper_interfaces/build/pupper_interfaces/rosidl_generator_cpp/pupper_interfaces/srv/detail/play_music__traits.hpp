// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pupper_interfaces:srv/PlayMusic.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__PLAY_MUSIC__TRAITS_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__PLAY_MUSIC__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pupper_interfaces/srv/detail/play_music__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const PlayMusic_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: file_name
  {
    out << "file_name: ";
    rosidl_generator_traits::value_to_yaml(msg.file_name, out);
    out << ", ";
  }

  // member: start_second
  {
    out << "start_second: ";
    rosidl_generator_traits::value_to_yaml(msg.start_second, out);
    out << ", ";
  }

  // member: duration
  {
    out << "duration: ";
    rosidl_generator_traits::value_to_yaml(msg.duration, out);
    out << ", ";
  }

  // member: num_loops
  {
    out << "num_loops: ";
    rosidl_generator_traits::value_to_yaml(msg.num_loops, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PlayMusic_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: file_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "file_name: ";
    rosidl_generator_traits::value_to_yaml(msg.file_name, out);
    out << "\n";
  }

  // member: start_second
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start_second: ";
    rosidl_generator_traits::value_to_yaml(msg.start_second, out);
    out << "\n";
  }

  // member: duration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "duration: ";
    rosidl_generator_traits::value_to_yaml(msg.duration, out);
    out << "\n";
  }

  // member: num_loops
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num_loops: ";
    rosidl_generator_traits::value_to_yaml(msg.num_loops, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PlayMusic_Request & msg, bool use_flow_style = false)
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
  const pupper_interfaces::srv::PlayMusic_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::PlayMusic_Request & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::PlayMusic_Request>()
{
  return "pupper_interfaces::srv::PlayMusic_Request";
}

template<>
inline const char * name<pupper_interfaces::srv::PlayMusic_Request>()
{
  return "pupper_interfaces/srv/PlayMusic_Request";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::PlayMusic_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::PlayMusic_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pupper_interfaces::srv::PlayMusic_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace pupper_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const PlayMusic_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PlayMusic_Response & msg,
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

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PlayMusic_Response & msg, bool use_flow_style = false)
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
  const pupper_interfaces::srv::PlayMusic_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  pupper_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pupper_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pupper_interfaces::srv::PlayMusic_Response & msg)
{
  return pupper_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pupper_interfaces::srv::PlayMusic_Response>()
{
  return "pupper_interfaces::srv::PlayMusic_Response";
}

template<>
inline const char * name<pupper_interfaces::srv::PlayMusic_Response>()
{
  return "pupper_interfaces/srv/PlayMusic_Response";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::PlayMusic_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pupper_interfaces::srv::PlayMusic_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pupper_interfaces::srv::PlayMusic_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<pupper_interfaces::srv::PlayMusic>()
{
  return "pupper_interfaces::srv::PlayMusic";
}

template<>
inline const char * name<pupper_interfaces::srv::PlayMusic>()
{
  return "pupper_interfaces/srv/PlayMusic";
}

template<>
struct has_fixed_size<pupper_interfaces::srv::PlayMusic>
  : std::integral_constant<
    bool,
    has_fixed_size<pupper_interfaces::srv::PlayMusic_Request>::value &&
    has_fixed_size<pupper_interfaces::srv::PlayMusic_Response>::value
  >
{
};

template<>
struct has_bounded_size<pupper_interfaces::srv::PlayMusic>
  : std::integral_constant<
    bool,
    has_bounded_size<pupper_interfaces::srv::PlayMusic_Request>::value &&
    has_bounded_size<pupper_interfaces::srv::PlayMusic_Response>::value
  >
{
};

template<>
struct is_service<pupper_interfaces::srv::PlayMusic>
  : std::true_type
{
};

template<>
struct is_service_request<pupper_interfaces::srv::PlayMusic_Request>
  : std::true_type
{
};

template<>
struct is_service_response<pupper_interfaces::srv::PlayMusic_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PUPPER_INTERFACES__SRV__DETAIL__PLAY_MUSIC__TRAITS_HPP_
