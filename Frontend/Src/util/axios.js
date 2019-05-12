import axios from 'axios';

axios.defaults.baseURL = process.env.BASE_API_URL;
axios.defaults.withCredentials = true;
axios.defaults.headers.post['Content-Type'] = "application/json";
axios.defaults.xsrfHeaderName = 'CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

export const setAuthorizationToken = (tokenString) => {
    axios.defaults.headers.common['Authorization'] = tokenString;
};

export const clearAuthorizationToken = () => {
    Reflect.deleteProperty(axios.defaults.headers.common, 'Authorization');
};

export default axios;
