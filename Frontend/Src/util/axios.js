import axios from 'axios';

const baseUrl = process.env.BASE_API_URL;

export default axios.create({
    withCredentials: true,
    baseURL: baseUrl,
    headers: {
        "Content-Type": "application/json"
    },
    xsrfHeaderName: "X-CSRFToken",
    xsrfCookieName: "csrftoken"
});
