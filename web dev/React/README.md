# React

## Resources

---

### Folder Structure

- [Blog - 1](https://medium.com/@Charles_Stover/optimal-file-structure-for-react-applications-f3e35ad0a145)
- [Blog - 2](https://latteandcode.medium.com/reactjs-the-folder-structure-i-feel-most-comfortable-with-694edaed0065)

---

### Class Component Lifecycle Method

| function                  | triggering point                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| constructor               | This will be first called                                                                     |
| componentWillMount        | immediately before initial rendering                                                          |
| componentDidMount         | immediately after initial rendering                                                           |
| componentWillReceiveProps | When component receive new props                                                              |
| shouldComponentUpdate     | Before rendering, after receiving new props or state (return false if you don't wanna render) |
| componentWill Update      | Before rendering, after receiving new props or state                                          |
| componentDidUpdate        | After component's update are flushed to DOM                                                   |
| componentWillUnmount      | Immediately before removing component from DOM                                                |
