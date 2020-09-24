import axios from "axios";
import url from "./Url.js";

const findComBykeyword = (keyword, callback, errorCallback) => {
    axios.get(url.url + '/' + keyword)
        .then(res => callback(res))
        .catch(err => errorCallback(err));
}

const findComAll = (data, callback, errorCallback) => {
    axios.get(url.url + '/company/')
        .then(res => callback(res))
        .catch(err => errorCallback(err));
}

const CompanyApi = {
    findComBykeyword: (data, callback, errorCallback) => findComBykeyword(data, callback, errorCallback),
    findComAll: (data, callback, errorCallback) => findComAll(data, callback, errorCallback)
}

export default CompanyApi