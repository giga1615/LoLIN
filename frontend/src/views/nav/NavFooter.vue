<template>
  <!-- 
    * 작성자 : 서울1반 4팀 윤지선
    * 내용 : foote text 수정
    * 생성일자 : 2021-03-24
    * 최종수정일자 : 2021-03-29
  -->

  <div>
    <!-- ======= Footer ======= -->
    <footer id="footer">
      <div class="footer-top">
        <div class="container">
          <div class="row">
            <div class="col-lg-3 col-md-6">
              <div class="footer-info">
                <h3>LoLin</h3>
                <p>
                  서울 강남구 테헤란로 212, <br />
                  싸피4기, 서울1반 A104<br /><br />
                  <strong>Tel:</strong> +82 02 3429 5114<br />
                  <strong>Email:</strong> lolin@ssafy.com<br />
                </p>
                <div class="social-links mt-3">
                  <router-link to="#" class="twitter"><i class="bx bxl-twitter"></i></router-link>
                  <router-link to="#" class="facebook"><i class="bx bxl-facebook"></i></router-link>
                  <router-link to="#" class="instagram"
                    ><i class="bx bxl-instagram"></i
                  ></router-link>
                  <router-link to="#" class="google-plus"><i class="bx bxl-skype"></i></router-link>
                  <router-link to="#" class="linkedin"><i class="bx bxl-linkedin"></i></router-link>
                </div>
              </div>
            </div>

            <div class="col-lg-2 col-md-6 footer-links">
              <h4>Useful Links</h4>
              <ul>
                <li><i class="bx bx-chevron-right"></i> <router-link to="#">Home</router-link></li>
                <li>
                  <i class="bx bx-chevron-right"></i> <router-link to="#">About us</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i> <router-link to="#">Services</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i>
                  <router-link to="#">Terms of service</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i>
                  <router-link to="#">Privacy policy</router-link>
                </li>
              </ul>
            </div>

            <div class="col-lg-3 col-md-6 footer-links">
              <h4>Our Services</h4>
              <ul>
                <li>
                  <i class="bx bx-chevron-right"></i> <router-link to="#">Web Design</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i>
                  <router-link to="#">Web Development</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i>
                  <router-link to="#">Product Management</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i> <router-link to="#">Marketing</router-link>
                </li>
                <li>
                  <i class="bx bx-chevron-right"></i>
                  <router-link to="#">Graphic Design</router-link>
                </li>
              </ul>
            </div>

            <div class="col-lg-4 col-md-6 footer-newsletter">
              <h4>Our Newsletter</h4>
              <p>Tamen quem nulla quae legam multos aute sint culpa legam noster magna</p>
              <form action="" method="post">
                <input type="email" name="email" /><input type="submit" value="Subscribe" />
              </form>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="copyright">
          &copy; Copyright <strong><span>돌멩이가뭐어때서</span></strong
          >. All Rights Reserved
        </div>
        <div class="credits">Made by <router-link to="#">서울 9반 스톤즈</router-link></div>
      </div>
    </footer>
    <!-- End Footer -->

    <router-link to="#" class="back-to-top"><i class="bx bxs-up-arrow-alt"></i></router-link>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
