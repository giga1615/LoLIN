package com.lolin.service;

import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.lolin.dao.LikeDao;
import com.lolin.model.LikeDto;

@Service
public class LikeServiceImpl implements LikeService {

	@Autowired
	private SqlSession session;

	@Override
	public void likePlus(String my_id, String my_nickname, String your_nickname) throws SQLException {

		session.getMapper(LikeDao.class).likeInsert(my_id, my_nickname, your_nickname);
		session.getMapper(LikeDao.class).likePlus(my_nickname, your_nickname);
	}

	@Override
	public void likeMinus(String my_nickname, String your_nickname) throws SQLException {
		session.getMapper(LikeDao.class).likeDelete(my_nickname, your_nickname);
		session.getMapper(LikeDao.class).likeMinus(my_nickname, your_nickname);
	}

	@Override
	public List<LikeDto> likeRead(String my_id) throws SQLException {

		return session.getMapper(LikeDao.class).likeRead(my_id);
	}

}
