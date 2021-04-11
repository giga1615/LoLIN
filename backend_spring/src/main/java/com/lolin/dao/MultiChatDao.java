package com.lolin.dao;

import java.sql.SQLException;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.lolin.model.MultiChatRoomMessageDto;
import com.lolin.model.ConnectionDto;
import com.lolin.model.MemberDto;
import com.lolin.model.MyRoomListDto;

@Repository
public interface MultiChatDao {

	void makeChatRoom(String id, String nickName, String roomName) throws SQLException;

	void enterToChatRoom(String id, String nickName, String roomName, String roomNumber) throws SQLException;// 채팅방 입장

	String getRoomNumberByRoomName(String roomName) throws SQLException;// 룸네임으로 룸번호 알아내기

	String getRoomNameByRoomNumber(int roomNumber) throws SQLException;// 룸번호로 룸이름 알아내기

	int getCountRoomMember(int roomNumber) throws SQLException;// 룸번호로 채팅방 인원수 알아내기

	List<MyRoomListDto> getMyRoomList(String id) throws SQLException;// 방장의 채팅방 목록

	List<MultiChatRoomMessageDto> getRoomsAllMessageByRoomNumber(String roomNumber) throws SQLException;// 채팅 디테일로 들어왔을때

	void sendMessageToChatRoom(MultiChatRoomMessageDto sendMessageDto) throws SQLException; // 센드 메세지

	List<String> getRoomMemberList(int roomNumber) throws SQLException;// 룸멤버 이름 다불러오기

	int connected(String id, String nickName) throws SQLException;

	int disConnected(String id) throws SQLException;

	ConnectionDto connectionCheck(String id) throws SQLException;
	
	String getBangJang(int roomNumber) throws SQLException;// 방장만 불러오기
	
}
