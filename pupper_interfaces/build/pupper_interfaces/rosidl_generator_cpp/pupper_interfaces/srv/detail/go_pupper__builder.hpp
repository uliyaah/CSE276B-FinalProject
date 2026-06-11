// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:srv/GoPupper.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__BUILDER_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/srv/detail/go_pupper__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_GoPupper_Request_command
{
public:
  Init_GoPupper_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::srv::GoPupper_Request command(::pupper_interfaces::srv::GoPupper_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::GoPupper_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::GoPupper_Request>()
{
  return pupper_interfaces::srv::builder::Init_GoPupper_Request_command();
}

}  // namespace pupper_interfaces


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_GoPupper_Response_executed
{
public:
  Init_GoPupper_Response_executed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::srv::GoPupper_Response executed(::pupper_interfaces::srv::GoPupper_Response::_executed_type arg)
  {
    msg_.executed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::GoPupper_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::GoPupper_Response>()
{
  return pupper_interfaces::srv::builder::Init_GoPupper_Response_executed();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__SRV__DETAIL__GO_PUPPER__BUILDER_HPP_
