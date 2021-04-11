package com.lolin.dao;

import java.sql.SQLException;

import org.springframework.stereotype.Repository;

import com.lolin.model.MemberDto;

@Repository
public interface LoginDao {

	// String으로 비밀번호 가져와서 체크만 되도록
	MemberDto login(String id) throws SQLException;

}
