import React from 'react';
import PropTypes from 'prop-types';
import { Form, Input, Button, Layout } from 'element-react';
import { connect } from 'react-redux';
import { push } from 'connected-react-router';
import { signup, clearSignup } from '../actions/auth';


export class Signup extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            form: {
                username: '',
                name: '',
                password: '',
                confirmPassword: ''
            },
            rules: {
                username: [
                    { required: true, message: 'Please input the username', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the username'));
                        } else if (this.props.error && this.props.error.username) {
                            callback(new Error(this.props.error.username));
                        } else {
                            callback();
                        }
                    } }
                ],
                name: [
                    { required: true, message: 'Please input name', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input name'));
                        } else if (this.props.error && this.props.error.name) {
                            callback(new Error(this.props.error.name));
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
                        } else if (this.props.error && this.props.error.password) {
                            callback(new Error(this.props.error.password));
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

    componentDidUpdate() {
        if (this.props.username) {
            this.props.redirectLogin();
        } else if (this.props.error) {
            this.refs.form.validate();
            this.props.clearSignup();
        }
    }

    handleSubmit(e) {
        e.preventDefault();

        this.refs.form.validate((valid) => {
            if (valid) {
                const user = Object.assign({}, this.state.form);
                Reflect.deleteProperty(user, 'confirmPassword');
                this.props.signup(user);
            } else {
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
                    <Form.Item label="Name" prop="name">
                        <Input type="text"
                            value={this.state.form.name}
                            onChange={this.onChange.bind(this, 'name')}
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
                        {/* <Button onClick={this.handleReset.bind(this)}>Reset</Button> */}
                    </Form.Item>
                </Form>
            </Layout.Row>
        );
    }
}

Signup.propTypes = {
    signup: PropTypes.func.isRequired,
    redirectLogin: PropTypes.func.isRequired,
    clearSignup: PropTypes.func.isRequired,
    error: PropTypes.shape({
        username: PropTypes.string,
        password: PropTypes.string,
        name: PropTypes.string
    }),
    username: PropTypes.string
};

const mapStateToProps = (state) => {
    return {
        error: state.auth.error,
        username: state.auth.username
    };
};

const mapDispatchToProps = (dispatch) => ({
    signup: (user) => dispatch(signup(user)),
    clearSignup: () => dispatch(clearSignup()),
    redirectLogin: () => dispatch(push('/login'))
});

export default connect(mapStateToProps, mapDispatchToProps)(Signup);
