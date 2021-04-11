package com.lolin.service;

import java.sql.SQLException;
import java.util.List;

import com.lolin.model.MemberDto;

public interface MemberService {
	void make(MemberDto member) throws SQLException;

	String makeHashPassword(String pw) throws SQLException;

	int makeRandomNumber(String nickName);

	void update(MemberDto member) throws SQLException;

	String getNickName(String id) throws SQLException;

	String getID(String nickName) throws SQLException;

	List<String> getAllNickName(String myNickName) throws SQLException;

	void authPre(String nickName, int iconNumber) throws SQLException; // 아이콘 넘버 db에 저장해서 나중에 판단하도록;

	int getAuthPreImg(String nickName) throws SQLException;// local에서 authpreImgNumber가져옴

	void delete(String id) throws SQLException;

	void pwUpdate(MemberDto member) throws SQLException;

	String getNickNameById(String id) throws SQLException;

	String getIdByNickName(String nickName) throws SQLException;

}
