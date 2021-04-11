package com.lolin.service;

import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.lolin.dao.DmDao;
import com.lolin.model.DmMessageDto;

@Service
public class DmServiceImpl implements DmService {

	@Autowired
	private SqlSession session;

	@Override
	public void sendDm(DmMessageDto sendMessage) throws Exception {
		session.getMapper(DmDao.class).sendDm(sendMessage);
	}

	@Override
	public List<DmMessageDto> readDmByNickName(String myNickName, String yourNickName) throws Exception {

		List<DmMessageDto> list = session.getMapper(DmDao.class).readDmByNickName(myNickName, yourNickName);

		// System.out.println(list);
		return list;
	}

	@Override
	public List<String> getDmList(String myId) throws Exception {
		return session.getMapper(DmDao.class).getDmList(myId);
	}

}
