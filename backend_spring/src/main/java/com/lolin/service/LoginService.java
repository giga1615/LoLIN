
package com.lolin.service;

import java.sql.SQLException;

import com.lolin.model.MemberDto;

public interface LoginService {

	String login(String id, String pw) throws SQLException;

}
