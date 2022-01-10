export const validateRegister = ({ username, email, password }) => {
  const errors = []
  if (username === '') errors.push('The username is missing')
  if (email === '') errors.push('The email is missing')
  if (password.password === '') errors.push('The password is missing')
  if (password.password !== password.confirm) errors.push('The password are not matching')
  return errors
}
