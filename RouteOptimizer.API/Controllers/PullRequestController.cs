using Microsoft.AspNetCore.Mvc;
using RouteOptimizer.Core.Services;

namespace RouteOptimizer.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PullRequestController : ControllerBase
    {
        private readonly PullRequestService _service;

        public PullRequestController(PullRequestService service)
        {
            _service = service ?? throw new ArgumentNullException(nameof(service));
        }

        [HttpPost("change-target-branch")]
        public IActionResult ChangeTargetBranch(string pullRequestId, string newTargetBranch)
        {
            try
            {
                if (string.IsNullOrWhiteSpace(pullRequestId))
                {
                    return BadRequest("Pull request ID cannot be null or empty");
                }

                if (string.IsNullOrWhiteSpace(newTargetBranch))
                {
                    return BadRequest("New target branch cannot be null or empty");
                }

                var updatedPullRequest = _service.ChangeTargetBranch(pullRequestId, newTargetBranch);
                return Ok(updatedPullRequest);
            }
            catch (ArgumentException ex)
            {
                return NotFound(ex.Message);
            }
            catch (Exception ex)
            {
                return StatusCode(500, ex.Message);
            }
        }
    }
}
