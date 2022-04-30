import axios from 'axios';
const API_URL = 'http://localhost:3000/api/auth/';
class AuthService {
  login(user) {
    return axios
      .post(API_URL + 'login', {
        username: user.username,
        password: user.password
      })
      .then(response => {
        if (response.data.accessToken) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;
      });
  }
  logout() {
    localStorage.removeItem('user');
  }
  register(user) {
    return axios.post(API_URL + 'register', {
      nombre: user.nombre,
      username: user.username,
      email: user.email,
      password: user.password,
      apellido1: user.apellido1,
      apellido2: user.apellido2,
      documento: user.documento,
      telefono: user.telefono,
      fechaNacimiento: user.fechaNacimiento,
    });
  }
}
export default new AuthService();
