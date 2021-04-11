package com.lolin.service;

import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.lolin.dao.MultiChatDao;
import com.lolin.model.MultiChatRoomMessageDto;
import com.lolin.model.ConnectionDto;
import com.lolin.model.MyRoomListDto;

@Service
public class MultiChatServiceImpl implements MultiChatService {

	@Autowired
	private SqlSession session;

	@Override
	public void makeChatRoom(String id, String nickName, String roomName) throws SQLException {

		System.out.println(id + nickName + roomName);
		session.getMapper(MultiChatDao.class).makeChatRoom(id, nickName, roomName);
	}

	@Override
	public void enterToChatRoom(String id, String memberNickName, String roomName, String roomNumber)
			throws SQLException {

		session.getMapper(MultiChatDao.class).enterToChatRoom(id, memberNickName, roomName, roomNumber);

	}

	@Override
	public String getRoomNumberByRoomName(String roomName) throws SQLException {

		return session.getMapper(MultiChatDao.class).getRoomNumberByRoomName(roomName);
	}

	@Override
	public String getRoomNameByRoomNumber(int roomNumber) throws SQLException {
		return session.getMapper(MultiChatDao.class).getRoomNameByRoomNumber(roomNumber);
	}

	@Override
	public List<MyRoomListDto> getMyRoomList(String id) throws SQLException {

		return session.getMapper(MultiChatDao.class).getMyRoomList(id);
	}

	@Override
	public List<MultiChatRoomMessageDto> getRoomsAllMessageByRoomNumber(String roomNumber) throws SQLException {

		return session.getMapper(MultiChatDao.class).getRoomsAllMessageByRoomNumber(roomNumber);
	}

	@Override
	public void sendMessageToChatRoom(MultiChatRoomMessageDto sendMessageDto) throws SQLException {
		session.getMapper(MultiChatDao.class).sendMessageToChatRoom(sendMessageDto);

	}

	@Override
	public List<String> getRoomMemberList(int roomNumber) throws SQLException {

		return session.getMapper(MultiChatDao.class).getRoomMemberList(roomNumber);
	}

	@Override
	public int connected(String id, String nickName) throws SQLException {

		return session.getMapper(MultiChatDao.class).connected(id, nickName);
	}

	@Override
	public int disConnected(String id) throws SQLException {

		return session.getMapper(MultiChatDao.class).disConnected(id);
	}

	@Override
	public ConnectionDto connectionCheck(String id) throws SQLException {
		return session.getMapper(MultiChatDao.class).connectionCheck(id);
	}

	@Override
	public int getCountRoomMember(int roomNumber) throws SQLException {
		return session.getMapper(MultiChatDao.class).getCountRoomMember(roomNumber);
	}
	

	
   @Override
    public String getBangJang(int roomNumber) throws SQLException {
        return session.getMapper(MultiChatDao.class).getBangJang(roomNumber);
    }
}
