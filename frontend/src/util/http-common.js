import axios from "axios";

// axios 객체 생성
export default axios.create({
    // baseURL: "http://localhost:8000/api",
    baseURL: "http://j3a105.p.ssafy.io/api",
    headers: {
        "Content-type": "application/json",
    },
});