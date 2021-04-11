package com.lolin.service;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.lolin.dao.LoginDao;
import com.lolin.dao.MemberDao;
import com.lolin.model.MemberDto;

@Service
public class MemberServiceImpl implements MemberService, UserDetailsService {

	@Autowired
	private SqlSession session;

	@Autowired
	RiotApiService riotApiService;

	@Override
	public void make(MemberDto member) throws SQLException {
		session.getMapper(MemberDao.class).make(member);

	}

	// sha256만들어주는 메소드
	@Override
	public String makeHashPassword(String pw) throws SQLException {

		MessageDigest md = null;
		try {
			md = MessageDigest.getInstance("SHA-256");
		} catch (NoSuchAlgorithmException e) {
			System.out.println("해쉬형성부 오류");
			e.printStackTrace();
		}
		md.update(pw.getBytes());

		return bytesToHex1(md.digest());

	}

	// sha256 서브 메소드
	public static String bytesToHex1(byte[] bytes) {
		StringBuilder builder = new StringBuilder();
		for (byte b : bytes) {
			builder.append(String.format("%02x", b));
		}

		return builder.toString().substring(5, builder.length() - 1);
	}

	public int makeRandomNumber(String nickName) {
		int myIconNumber = 0;
		try {

			myIconNumber = Integer.parseInt(riotApiService.getLolProfileID(nickName));

		} catch (NumberFormatException | SQLException e) {

			e.printStackTrace();
		}

		while (true) {
			int randomNumber = (int) (Math.random() * 20) + 1;
			if (myIconNumber != randomNumber) {
				return randomNumber;
			}
		}

	}

	@Override
	public void authPre(String nickName, int iconNumber) throws SQLException {
		// iconNumber를 db에 집어넣어주고 나중에 체크해줌
		session.getMapper(MemberDao.class).authPre(nickName, iconNumber);

	}

	@Override
	public int getAuthPreImg(String nickName) throws SQLException {

		int ImgNumberLocal = session.getMapper(MemberDao.class).getAuthPreImg(nickName);

		return ImgNumberLocal;
	}

	@Override
	public void update(MemberDto member) throws SQLException {

		session.getMapper(MemberDao.class).update(member);

	}

	@Override
	public String getNickName(String id) throws SQLException {

		return session.getMapper(MemberDao.class).getNickName(id);
	}

	@Override
	public String getID(String nickName) throws SQLException {

		return session.getMapper(MemberDao.class).getID(nickName);
	}

	@Override
	public void delete(String id) throws SQLException {
		session.getMapper(MemberDao.class).delete(id);

	}

	@Override
	public void pwUpdate(MemberDto member) throws SQLException {
		session.getMapper(MemberDao.class).pwUpdate(member);
	}

	@Override
	public String getNickNameById(String id) throws SQLException {
		return session.getMapper(MemberDao.class).getNickNameById(id);
	}

	@Override
	public String getIdByNickName(String nickName) throws SQLException {
		return session.getMapper(MemberDao.class).getIdByNickName(nickName);
	}

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

		return null;
	}

	@Override
	public List<String> getAllNickName(String myNickName) throws SQLException {
		return session.getMapper(MemberDao.class).getAllNickName(myNickName);
	}

}
