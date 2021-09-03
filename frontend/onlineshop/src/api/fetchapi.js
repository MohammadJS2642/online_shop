const FetchData = async() => {
    const response = await fetch('http://127.0.0.1:8000/users/?format=json');
    const data = await response.json();
    return data;
}

export default FetchData;