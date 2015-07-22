#pragma once

#define NYTRAM_API __declspec(dllexport)

#if __cplusplus
extern "C" {
#endif

	unsigned int Add_World();
	
#if __cplusplus
}
#endif