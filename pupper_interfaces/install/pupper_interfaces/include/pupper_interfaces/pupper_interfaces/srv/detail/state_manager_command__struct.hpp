// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pupper_interfaces:srv/StateManagerCommand.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_HPP_
#define PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'command'
#include "pupper_interfaces/msg/detail/command__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Request __attribute__((deprecated))
#else
# define DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Request __declspec(deprecated)
#endif

namespace pupper_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StateManagerCommand_Request_
{
  using Type = StateManagerCommand_Request_<ContainerAllocator>;

  explicit StateManagerCommand_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_init)
  {
    (void)_init;
  }

  explicit StateManagerCommand_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _command_type =
    pupper_interfaces::msg::Command_<ContainerAllocator>;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const pupper_interfaces::msg::Command_<ContainerAllocator> & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Request
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Request
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StateManagerCommand_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const StateManagerCommand_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StateManagerCommand_Request_

// alias to use template instance with default allocator
using StateManagerCommand_Request =
  pupper_interfaces::srv::StateManagerCommand_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pupper_interfaces


#ifndef _WIN32
# define DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Response __attribute__((deprecated))
#else
# define DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Response __declspec(deprecated)
#endif

namespace pupper_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StateManagerCommand_Response_
{
  using Type = StateManagerCommand_Response_<ContainerAllocator>;

  explicit StateManagerCommand_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit StateManagerCommand_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Response
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pupper_interfaces__srv__StateManagerCommand_Response
    std::shared_ptr<pupper_interfaces::srv::StateManagerCommand_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StateManagerCommand_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const StateManagerCommand_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StateManagerCommand_Response_

// alias to use template instance with default allocator
using StateManagerCommand_Response =
  pupper_interfaces::srv::StateManagerCommand_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pupper_interfaces

namespace pupper_interfaces
{

namespace srv
{

struct StateManagerCommand
{
  using Request = pupper_interfaces::srv::StateManagerCommand_Request;
  using Response = pupper_interfaces::srv::StateManagerCommand_Response;
};

}  // namespace srv

}  // namespace pupper_interfaces

#endif  // PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_HPP_
