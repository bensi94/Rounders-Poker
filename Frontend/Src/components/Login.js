import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Form, Input, Button, Layout, Notification } from 'element-react';
import { push } from 'connected-react-router';

import { clearSignup, clearLogin, login } from '../actions/auth';
import { checkUser } from '../actions/user';


export class Login extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            form: {
                username: '',
                password: ''
            },
            rules: {
                username: [
                    { required: true, message: 'Please input the username', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the username'));
                        } else if (this.props.error) {
                            callback(new Error(this.props.error));
                        } else {
                            callback();
                        }
                    } }
                ],
                password: [
                    { required: true, message: 'Please input the password ', trigger: 'blur' },
                    { validator: (rule, value, callback) => {
                        if (value === '') {
                            callback(new Error('Please input the password'));
                        } else {
                            callback();
                        }
                    } }
                ]
            }
        };

        this.notification = this.notification.bind(this);
    }

    componentDidMount() {
        if (this.props.username) {
            this.notification(this.props.username);
            this.props.clearSignup();
        }
    }

    componentDidUpdate() {
        if (this.props.token && this.props.isAuthenticated) {
            this.props.redirectGame();
        } else if (this.props.error) {
            this.refs.form.validate();
            this.props.clearLogin();
        }
    }


    handleSubmit(e) {
        e.preventDefault();

        this.refs.form.validate((valid) => {
            if (valid) {
                this.props.login(this.state.form).then(() => {
                    this.props.checkUser().then(() => {
                        this.props.redirectGame();
                    });
                });
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

    notification(name) {
        // eslint-disable-next-line new-cap
        Notification({
            title: 'User created',
            message: 'Created new user: ' + name,
            type: 'success'
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
                    <h2 className="signup-login-title">Login</h2>
                    <Form.Item label="Username" prop="username">
                        <Input type="text"
                            value={this.state.form.username}
                            onChange={this.onChange.bind(this, 'username')}
                        />
                    </Form.Item>
                    <Form.Item label="Pasword" prop="password">
                        <Input type="password"
                            value={this.state.form.password}
                            onChange={this.onChange.bind(this, 'password')}
                        />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" onClick={this.handleSubmit.bind(this)}>Login</Button>
                        <Button onClick={this.handleReset.bind(this)}>Reset</Button>
                    </Form.Item>
                </Form>
            </Layout.Row>
        );
    }
}

Login.propTypes = {
    clearSignup: PropTypes.func.isRequired,
    clearLogin: PropTypes.func.isRequired,
    login: PropTypes.func.isRequired,
    redirectGame: PropTypes.func.isRequired,
    checkUser: PropTypes.func.isRequired,
    username: PropTypes.string,
    token: PropTypes.string,
    error: PropTypes.string,
    isAuthenticated: PropTypes.bool
};

const mapStateToProps = (state) => {
    return {
        username: state.auth.username,
        token: state.auth.token,
        error: state.auth.error,
        isAuthenticated: state.user.isAuthenticated
    };
};

const mapDispatchToProps = (dispatch) => ({
    clearSignup: () => dispatch(clearSignup()),
    clearLogin: () => dispatch(clearLogin()),
    login: (user) => dispatch(login(user)),
    redirectGame: () => dispatch(push('/game')),
    checkUser: () => dispatch(checkUser())
});

export default connect(mapStateToProps, mapDispatchToProps)(Login);
