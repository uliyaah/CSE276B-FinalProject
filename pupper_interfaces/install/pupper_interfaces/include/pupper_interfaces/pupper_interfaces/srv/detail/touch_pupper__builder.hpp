// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:srv/TouchPupper.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__BUILDER_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/srv/detail/touch_pupper__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_TouchPupper_Request_duration
{
public:
  explicit Init_TouchPupper_Request_duration(::pupper_interfaces::srv::TouchPupper_Request & msg)
  : msg_(msg)
  {}
  ::pupper_interfaces::srv::TouchPupper_Request duration(::pupper_interfaces::srv::TouchPupper_Request::_duration_type arg)
  {
    msg_.duration = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::TouchPupper_Request msg_;
};

class Init_TouchPupper_Request_command
{
public:
  Init_TouchPupper_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TouchPupper_Request_duration command(::pupper_interfaces::srv::TouchPupper_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_TouchPupper_Request_duration(msg_);
  }

private:
  ::pupper_interfaces::srv::TouchPupper_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::TouchPupper_Request>()
{
  return pupper_interfaces::srv::builder::Init_TouchPupper_Request_command();
}

}  // namespace pupper_interfaces


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_TouchPupper_Response_executed
{
public:
  Init_TouchPupper_Response_executed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::srv::TouchPupper_Response executed(::pupper_interfaces::srv::TouchPupper_Response::_executed_type arg)
  {
    msg_.executed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::TouchPupper_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::TouchPupper_Response>()
{
  return pupper_interfaces::srv::builder::Init_TouchPupper_Response_executed();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__BUILDER_HPP_
