package com.lolin.service;

import java.util.Map;

import com.lolin.model.UserInfoFromDjangoDto;

public interface DjangoService {

	double getTimeFromDjango(String nickName);

	UserInfoFromDjangoDto getUserInfoFromDjango(String nickName);

}
