/// SOLUTION OF DSA MOCK TEST 3 ANS//////

///QUESTION--1/////

class Stack {
    constructor() {
      this.stack = [];
    }
  
    push(element) {
      this.stack.push(element);
    }
  
    pop() {
      if (this.isEmpty()) {
        return "Stack is empty. Cannot pop an element.";
      }
      return this.stack.pop();
    }
  
    isEmpty() {
      return this.stack.length === 0;
    }
  }
  
  // Usage example:
  const stack = new Stack();
  stack.push(1);
  stack.push(2);
  stack.push(3);
  
  console.log(stack.pop()); // 3
  console.log(stack.pop()); // 2
  console.log(stack.isEmpty()); // false
  console.log(stack.pop()); // 1
  console.log(stack.pop()); // Stack is empty. Cannot pop an element.
  console.log(stack.isEmpty()); // true

  
///QUESTION--2/////

class Queue {
    constructor() {
      this.queue = [];
    }
  
    enqueue(element) {
      this.queue.push(element);
    }
  
    dequeue() {
      if (this.isEmpty()) {
        return "Queue is empty. Cannot dequeue an element.";
      }
      return this.queue.shift();
    }
  
    isEmpty() {
      return this.queue.length === 0;
    }
  }
  
  // Usage example:
  const queue = new Queue();
  queue.enqueue(4);
  queue.enqueue(5);
  queue.enqueue(6);
  
  console.log(queue.dequeue()); // 4
  console.log(queue.dequeue()); // 5
  console.log(queue.isEmpty()); // false
  console.log(queue.dequeue()); // 6
  console.log(queue.dequeue()); // Queue is empty. Cannot dequeue an element.
  console.log(queue.isEmpty()); // true
  
