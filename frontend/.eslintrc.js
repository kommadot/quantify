module.exports = {
  root: false,
  env: {
    node: false,
  },
  extends: 'vuetify',
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },
  "globals": {
    "$": true
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
}
