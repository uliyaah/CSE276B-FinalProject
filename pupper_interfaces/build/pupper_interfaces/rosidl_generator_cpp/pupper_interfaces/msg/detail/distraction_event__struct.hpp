// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pupper_interfaces:msg/DistractionEvent.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_HPP_
#define PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__pupper_interfaces__msg__DistractionEvent __attribute__((deprecated))
#else
# define DEPRECATED__pupper_interfaces__msg__DistractionEvent __declspec(deprecated)
#endif

namespace pupper_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DistractionEvent_
{
  using Type = DistractionEvent_<ContainerAllocator>;

  explicit DistractionEvent_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->duration = 0.0f;
    }
  }

  explicit DistractionEvent_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->duration = 0.0f;
    }
  }

  // field types and members
  using _duration_type =
    float;
  _duration_type duration;

  // setters for named parameter idiom
  Type & set__duration(
    const float & _arg)
  {
    this->duration = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> *;
  using ConstRawPtr =
    const pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pupper_interfaces__msg__DistractionEvent
    std::shared_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pupper_interfaces__msg__DistractionEvent
    std::shared_ptr<pupper_interfaces::msg::DistractionEvent_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DistractionEvent_ & other) const
  {
    if (this->duration != other.duration) {
      return false;
    }
    return true;
  }
  bool operator!=(const DistractionEvent_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DistractionEvent_

// alias to use template instance with default allocator
using DistractionEvent =
  pupper_interfaces::msg::DistractionEvent_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_HPP_
