package com.lolin.dao;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

import org.springframework.security.core.userdetails.User;
import org.springframework.stereotype.Repository;

import com.lolin.model.MemberDto;

@Repository
public interface MemberDao {

	void make(MemberDto member) throws SQLException;

	void update(MemberDto member) throws SQLException;

	String getNickName(String id) throws SQLException;

	String getID(String nickName) throws SQLException;

	List<String> getAllNickName(String myNickName) throws SQLException;

	void authPre(String nickName, int iconNumber) throws SQLException;

	int getAuthPreImg(String nickName) throws SQLException;

	String getNickNameById(String id) throws SQLException;

	void delete(String id) throws SQLException;

	void pwUpdate(MemberDto member) throws SQLException;

	String getIdByNickName(String nickName) throws SQLException;

	Optional<User> findByEmail(String username);
	
	String get_api_key() throws SQLException;

}
