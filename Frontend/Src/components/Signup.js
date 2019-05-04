import React from 'react';
import { Form, Input, Button, Layout } from 'element-react';


class Signup extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            form: {
                username: '',
                password: '',
                confirmPassword: ''
            },
            rules: {
                username: [
                    { required: true, message: 'Please input the username', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the username'));
                        } else {
                            callback();
                        }
                    } }
                ],
                password: [
                    { required: true, message: 'Please input the password', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the password'));
                        } else if (value.length < 5) {
                            callback(new Error('Password must be at least 5 characters'));
                        } else {
                            if (this.state.form.confirmPassword !== '') {
                                this.refs.form.validateField('confirmPassword');
                            }
                            callback();
                        }
                    } }
                ],
                confirmPassword: [
                    { required: true, message: 'Please input the password again', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the password again'));
                        } else if (value !== this.state.form.password) {
                            callback(new Error('The passwords do not match'));
                        } else {
                            callback();
                        }
                    } }
                ]
            }
        };
    }

    handleSubmit(e) {
        e.preventDefault();

        this.refs.form.validate((valid) => {
            if (valid) {
                console.log('isValid');
            } else {
                console.log('invalid');
                return false;
            }
        });
    }

    handleReset(e) {
        e.preventDefault();

        this.refs.form.resetFields();
    }

    onChange(key, value) {
        this.setState({
            form: Object.assign({}, this.state.form, { [key]: value })
        });
    }

    render() {
        return (
            <Layout.Row type="flex" justify="center">
                <Form ref="form"
                    model={this.state.form}
                    rules={this.state.rules}
                    labelWidth="100"
                    className="signup-login-form"
                >
                    <h2 className="signup-login-title">Sign up</h2>
                    <Form.Item label="Username" prop="username">
                        <Input type="text"
                            value={this.state.form.username}
                            onChange={this.onChange.bind(this, 'username')}
                            autoComplete="off"
                        />
                    </Form.Item>
                    <Form.Item label="Pasword" prop="password">
                        <Input type="password"
                            value={this.state.form.password}
                            onChange={this.onChange.bind(this, 'password')}
                            autoComplete="off"
                        />
                    </Form.Item>
                    <Form.Item label="Confirm password" prop="confirmPassword">
                        <Input type="password"
                            value={this.state.form.confirmPassword}
                            onChange={this.onChange.bind(this, 'confirmPassword')}
                            autoComplete="off"
                        />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" onClick={this.handleSubmit.bind(this)}>Sign up</Button>
                        <Button onClick={this.handleReset.bind(this)}>Reset</Button>
                    </Form.Item>
                </Form>
            </Layout.Row>
        );
    }
}

export default Signup;
