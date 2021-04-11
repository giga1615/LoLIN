module.exports = {
  devServer: {
    proxy: {
      '/server1/Ingame': {
        target: 'http://j4a104.p.ssafy.io:8080/api',
        changeOrigin: true,
      },
      '/member/make/auth/makeRandomNumber': {
        target: 'http://j4a104.p.ssafy.io:8080/api',
        changeOrigin: true,
      },
      '/member/executeInitPredictTime': {
        target: 'http://j4a104.p.ssafy.io:8080/api',
        changeOrigin: true,
      },
      '/file/upload': {
        target: 'http://j4a104.p.ssafy.io:8080/api',
        changeOrigin: true,
      },
      '/like/ilikeU/readMyList': {
        target: 'http://j4a104.p.ssafy.io:8080/api',
        changeOrigin: true,
      },
    },
  },
};
