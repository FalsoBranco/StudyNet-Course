export const validateLogin = ({ username, password }) => {
  const errors = []
  if (username === '') {
    errors.push('The username is missing')
  }
  if (password === '') {
    errors.push('The password is missing')
  }
  return errors
}
