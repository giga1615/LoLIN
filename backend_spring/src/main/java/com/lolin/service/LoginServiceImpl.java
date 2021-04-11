package com.lolin.service;

import java.sql.SQLException;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.lolin.dao.LoginDao;
import com.lolin.model.MemberDto;

@Service
public class LoginServiceImpl implements LoginService {

	@Autowired
	private SqlSession session;

	@Override
	public String login(String id, String pw) throws SQLException {

		MemberDto member = session.getMapper(LoginDao.class).login(id);

		if (member == null) {
			return "NO";
		}
		boolean loginCheck = pw.equals(member.getPw());

		if (loginCheck == true) {
			return "YES";
		} else {
			return "NO";
		}

	}

}
