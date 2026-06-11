// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:msg/Command.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__COMMAND__BUILDER_HPP_
#define PUPPER_INTERFACES__MSG__DETAIL__COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/msg/detail/command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace msg
{

namespace builder
{

class Init_Command_command
{
public:
  Init_Command_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::msg::Command command(::pupper_interfaces::msg::Command::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::msg::Command msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::msg::Command>()
{
  return pupper_interfaces::msg::builder::Init_Command_command();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__MSG__DETAIL__COMMAND__BUILDER_HPP_
