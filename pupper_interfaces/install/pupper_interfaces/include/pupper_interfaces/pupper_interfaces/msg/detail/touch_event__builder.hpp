// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__BUILDER_HPP_
#define PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pupper_interfaces/msg/detail/touch_event__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pupper_interfaces
{

namespace msg
{

namespace builder
{

class Init_TouchEvent_location
{
public:
  Init_TouchEvent_location()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pupper_interfaces::msg::TouchEvent location(::pupper_interfaces::msg::TouchEvent::_location_type arg)
  {
    msg_.location = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pupper_interfaces::msg::TouchEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pupper_interfaces::msg::TouchEvent>()
{
  return pupper_interfaces::msg::builder::Init_TouchEvent_location();
}

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__BUILDER_HPP_
