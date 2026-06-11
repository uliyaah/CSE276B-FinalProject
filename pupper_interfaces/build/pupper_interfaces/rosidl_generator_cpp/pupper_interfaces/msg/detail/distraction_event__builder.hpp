// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:msg/DistractionEvent.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__BUILDER_HPP_
#define PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/msg/detail/distraction_event__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace msg
{

namespace builder
{

class Init_DistractionEvent_duration
{
public:
  Init_DistractionEvent_duration()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::msg::DistractionEvent duration(::pupper_interfaces::msg::DistractionEvent::_duration_type arg)
  {
    msg_.duration = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::msg::DistractionEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::msg::DistractionEvent>()
{
  return pupper_interfaces::msg::builder::Init_DistractionEvent_duration();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__BUILDER_HPP_
