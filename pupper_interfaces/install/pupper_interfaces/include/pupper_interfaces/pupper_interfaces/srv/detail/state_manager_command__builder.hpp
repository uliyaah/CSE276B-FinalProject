// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:srv/StateManagerCommand.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__BUILDER_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/srv/detail/state_manager_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_StateManagerCommand_Request_command
{
public:
  Init_StateManagerCommand_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::srv::StateManagerCommand_Request command(::pupper_interfaces::srv::StateManagerCommand_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::StateManagerCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::StateManagerCommand_Request>()
{
  return pupper_interfaces::srv::builder::Init_StateManagerCommand_Request_command();
}

}  // namespace pupper_interfaces


namespace pupper_interfaces
{

namespace srv
{

namespace builder
{

class Init_StateManagerCommand_Response_success
{
public:
  Init_StateManagerCommand_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::srv::StateManagerCommand_Response success(::pupper_interfaces::srv::StateManagerCommand_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::srv::StateManagerCommand_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::srv::StateManagerCommand_Response>()
{
  return pupper_interfaces::srv::builder::Init_StateManagerCommand_Response_success();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__BUILDER_HPP_
