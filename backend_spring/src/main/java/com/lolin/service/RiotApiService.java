package com.lolin.service;

import java.sql.SQLException;

public interface RiotApiService {

	String getLolProfileID(String nickName) throws SQLException;

}
